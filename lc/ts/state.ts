import { Language } from "./language.ts";

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
  }

  interface SolutionDetails {
    leetcodeId: string;
    leetcodeSlug: string;
    language: Language.Type;
    timeStarted: string;
    successfulSubmissions: Submission[];
    failedSubmissions: Submission[];
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
      Object.values(firstSolveMap).reduce((previous, current) => {
        const firstSuccessDateStr = current.successfulSubmissions[0].date;
        const firstSuccess = firstSuccessDateStr
          ? new Date(firstSuccessDateStr)
          : new Date();
        const start = new Date(current.timeStarted);
        return previous + (firstSuccess.getTime() - start.getTime()) / 1000;
      }, 0) / Object.keys(firstSolveMap).length
    );
  };
}
