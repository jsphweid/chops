import { client } from "./client.ts";

interface SubmissionStatusPending {
  state: "PENDING" | "STARTED";
}

interface SubmissionStatusSuccessBase {
  submission_id: string;
  total_testcases: number;
  total_correct: number;
}

interface SubmissionStatusRejectedResponse extends SubmissionStatusSuccessBase {
  state: "SUCCESS";
  status_msg: "Wrong Answer" | "Runtime Error";
  last_testcase: string;
  expected_output: string;
  runtime_error?: string;
  full_runtime_error?: string;
}

interface SubmissionStatusAcceptedResponse extends SubmissionStatusSuccessBase {
  state: "SUCCESS";
  status_msg: "Accepted";
  runtime_percentile: number;
  memory_percentile: number;
  status_memory: string;
}

export type SubmissionCheckSuccessResponse =
  | SubmissionStatusRejectedResponse
  | SubmissionStatusAcceptedResponse;

export type SubmissionCheckResponse =
  | SubmissionStatusPending
  | SubmissionCheckSuccessResponse;

export const isSubmissionCheckPending = (
  response: SubmissionCheckResponse
): response is SubmissionStatusPending =>
  response.state === "PENDING" || response.state == "STARTED";

export const isSubmissionCheckAccepted = (
  response: SubmissionCheckResponse
): response is SubmissionStatusAcceptedResponse =>
  (response as any).status_msg === "Accepted";

export const isSubmissionCheckRejected = (
  response: SubmissionCheckResponse
): response is SubmissionStatusRejectedResponse =>
  !isSubmissionCheckPending(response) &&
  (response as any).status_msg !== "Accepted";

export const checkSubmission = (
  submissionId: string | number
): Promise<SubmissionCheckResponse> =>
  client
    .get(`/submissions/detail/${submissionId}/check/`)
    .then((response) => response.data);
