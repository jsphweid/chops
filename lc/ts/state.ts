import { Language } from "./language.ts";
import { Utils } from "./utils.ts";

export namespace State {
  export enum SubmissionType {
    // NOTE: DO NOT CHANGE THIS
    FailedSubmission = "FAIL",
    SuccessfulSubmission = "SUCCESS",
  }

  interface Submission {
    date: string;
    leetcodeSubmissionId: string;
    type: SubmissionType;
    failureReason?: string;
  }

  interface SolutionDetails {
    leetcodeId: string;
    leetcodeSlug: string;
    language: Language.Type;
    timeStarted: string;
    successfulSubmissions: Submission[];
    failedSubmissions: Submission[];
  }

  export interface Redo {
    slug: string;
    representation: string;
    daysSinceLast: number;
    step: number;
  }

  interface Type {
    solutions: {
      [filepath: string]: SolutionDetails;
    };
  }

  const emptyState: Type = {
    solutions: {},
  };

  const relativePath = "state.json";

  const loadState = (): Type => {
    let state = emptyState;
    try {
      state = JSON.parse(Deno.readTextFileSync("state.json"));
    } catch (e) {}
    return state;
  };

  const writeState = (state: Type): void => {
    Deno.writeTextFileSync(relativePath, JSON.stringify(state));
  };

  export const startNewSolution = (
    leetcodeId: string,
    leetcodeSlug: string,
    language: Language.Type,
    filepath: string
  ): Date => {
    const state = loadState();
    if (state.solutions[filepath]) {
      throw new Error("Solution already exists... cannot create a new one!");
    }
    const startTime = new Date();
    state.solutions[filepath] = {
      leetcodeId,
      leetcodeSlug,
      language,
      timeStarted: startTime.toISOString(),
      successfulSubmissions: [],
      failedSubmissions: [],
    };
    writeState(state);
    return startTime;
  };

  export const registerSubmission = (
    filepath: string,
    submission: Submission
  ): void => {
    const state = loadState();
    if (!state.solutions[filepath]) {
      throw new Error(
        `Solution for ${filepath} doesn't exist or hasn't been started...`
      );
    }
    const key =
      submission.type === SubmissionType.FailedSubmission
        ? "failedSubmissions"
        : "successfulSubmissions";
    state.solutions[filepath][key].push(submission);
    writeState(state);
  };

  export const getSolutionDetails = (
    filepath: string
  ): SolutionDetails | null => loadState().solutions[filepath];

  // TODO: it'd probably be simpler to just put this on the details object itself,
  // but this change would require a data migration
  const getProblemNameFromKey = (key: string): string => key.split("/")[1];

  export const getAverageSecondsToFirstSolve = () => {
    const state = loadState();

    // TODO: in the future, this should return a breakdown by easy, medium, hard

    // build map of the first time a solution was made with each problem
    const firstSolveMap: { [problem: string]: SolutionDetails } = {};
    Object.entries(state.solutions).forEach(([key, details]) => {
      const leetcodeProblemName = getProblemNameFromKey(key);
      if (
        !firstSolveMap[leetcodeProblemName] ||
        details.timeStarted < firstSolveMap[leetcodeProblemName].timeStarted
      ) {
        firstSolveMap[leetcodeProblemName] = details;
      }
    });

    // average the first success for all the first solves together...
    return (
      Object.values(firstSolveMap)
        .filter((solutionDetails) => solutionDetails.successfulSubmissions[0])
        .reduce((previous, current) => {
          const firstSuccessDateStr = current.successfulSubmissions[0].date;
          const firstSuccess = firstSuccessDateStr
            ? new Date(firstSuccessDateStr)
            : new Date();
          const start = new Date(current.timeStarted);
          return previous + (firstSuccess.getTime() - start.getTime()) / 1000;
        }, 0) / Object.keys(firstSolveMap).length
    );
  };

  export const getUnsolvedProblems = () =>
    Object.entries(loadState().solutions)
      .filter(([_, value]) => !value.successfulSubmissions)
      .map(
        ([key, value]) =>
          `${value.timeStarted} - ${value.leetcodeSlug} - ${key}`
      );

  const getNextDate = (dates: Date[]) => {
    // get's next date based on a schedule
    // reduces datetime -> date based on local day
    const order = [0, 1, 3, 7, 14, 30];

    const format = (date: Date) =>
      // ensures reduced date is in local timezone
      Utils.formatDate(new Date(date.toLocaleString().split(" ")[0]));

    const datesGrouped: Record<string, Date[]> = {};
    const datesSorted = dates.sort();
    datesSorted.forEach((date) => {
      const stringDate = format(date);
      if (datesGrouped[stringDate]) {
        datesGrouped[stringDate].push(date);
      } else {
        datesGrouped[stringDate] = [date];
      }
    });

    const nextPosition = Object.keys(datesGrouped).length;
    const nextIndex = Math.min(nextPosition, order.length - 1);
    const nextSpan = order[nextIndex];

    const representation = [...order] as Array<string | number>;
    representation[nextIndex] = `[${order[nextIndex]}]`;
    return {
      step: nextIndex,
      representation: JSON.stringify(representation),
      nextDate: Utils.addDays(datesSorted[dates.length - 1], nextSpan),
    };
  };

  const getSolvedProblems = () => {
    const groupedBySlug: Record<string, Date[]> = {};
    Object.entries(loadState().solutions).forEach(([key, value]) => {
      const slug = key.split("/")[1];
      if (value.successfulSubmissions.length) {
        const date = new Date(value.successfulSubmissions[0].date);
        if (groupedBySlug[slug]) {
          groupedBySlug[slug].push(date);
        } else {
          groupedBySlug[slug] = [date];
        }
      }
    });
    return groupedBySlug;
  };

  const prioritizeRedos = (redos: Array<Redo>): Array<Redo> =>
    // prioritize lower steps
    // if on same step, priorize for bigger daysSinceLast
    redos.sort((a, b) => {
      if (a.step > b.step) {
        return 1;
      } else if (b.step < a.step) {
        return -1;
      } else {
        if (a.daysSinceLast > b.daysSinceLast) {
          return -1;
        } else if (b.daysSinceLast > a.daysSinceLast) {
          return 1;
        } else {
          return 0;
        }
      }
    });

  export const getRedos = (): Array<Redo> => {
    const state = loadState();
    const redos: Array<Redo> = [];
    const now = new Date();
    for (const [slug, dates] of Object.entries(getSolvedProblems())) {
      const { representation, nextDate, step } = getNextDate(dates);
      if (nextDate < now) {
        redos.push({
          slug,
          step,
          representation,
          daysSinceLast: Utils.getDiffDays(nextDate, now),
        });
      }
    }
    return prioritizeRedos(redos);
  };
}
