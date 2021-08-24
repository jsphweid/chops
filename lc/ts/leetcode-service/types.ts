import { Question as RawRequestQuestion } from "./raw-requests/get-question-by-slug.ts";
import { SuggestedQuestion } from "./raw-requests/get-suggested-questions.ts";
import * as RawRequestSubmission from "./raw-requests/check-submission.ts";

export interface ParsedUserFile {
  sessionCSRF: string;
  sessionId: string;
}

export namespace Question {
  export type Type = RawRequestQuestion;
}

export namespace SuggestedQuestion {
  export type Type = SuggestedQuestion;
}

export namespace Submission {
  export type Type = Accepted | Rejected;

  export const isAccepted = (submission: Type): submission is Accepted =>
    submission.statusMessage === "Accepted";

  export const isRejected = (submission: Type): submission is Rejected =>
    submission.statusMessage !== "Accepted";

  export const fromRaw = (
    raw: RawRequestSubmission.SubmissionCheckSuccessResponse
  ): Type =>
    RawRequestSubmission.isSubmissionCheckAccepted(raw)
      ? {
          submissionId: raw.submission_id,
          totalTestcases: raw.total_testcases,
          totalCorrect: raw.total_correct,
          statusMessage: raw.status_msg,
          runtimePercentile: raw.runtime_percentile,
          memoryPercentile: raw.memory_percentile,
          statusMemory: raw.status_memory,
        }
      : {
          submissionId: raw.submission_id,
          totalTestcases: raw.total_testcases,
          totalCorrect: raw.total_correct,
          statusMessage: raw.status_msg,
          lastTestcase: raw.last_testcase,
          expectedOutput: raw.expected_output,
          runtimeError: raw.runtime_error,
          fullRuntimeError: raw.full_runtime_error,
        };

  export interface Accepted {
    submissionId: string;
    totalTestcases: number;
    totalCorrect: number;
    statusMessage: "Accepted";
    runtimePercentile: number;
    memoryPercentile: number;
    statusMemory: string;
  }

  export interface Rejected {
    submissionId: string;
    totalTestcases: number;
    totalCorrect: number;
    statusMessage: "Wrong Answer" | "Runtime Error";
    lastTestcase: string;
    expectedOutput: string;
    runtimeError?: string;
    fullRuntimeError?: string;
  }
}
