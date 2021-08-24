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
}
