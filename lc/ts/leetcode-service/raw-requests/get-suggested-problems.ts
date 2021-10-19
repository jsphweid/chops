import { client } from "./client.ts";
import { getSuggestedProblemsQuery } from "./queries.ts";
import { Difficulty } from "../../difficulty.ts";

export interface SuggestedProblem {
  problemId: string;
  title: string;
  titleSlug: string;
  difficulty: string;
  isPaidOnly: boolean;
}

export type Difficulty = "EASY" | "MEDIUM" | "HARD";

interface GetSuggestedProblemsResponse {
  problem: SuggestedProblem;
}

export const getSuggestedProblems = (
  difficulty: Difficulty
): Promise<SuggestedProblem[]> =>
  client
    .post("/graphql", getSuggestedProblemsQuery(difficulty, 10))
    .then((response) => response.data.data.problemsetProblemList.problems);
