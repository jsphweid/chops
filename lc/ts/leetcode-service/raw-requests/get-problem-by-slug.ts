import { client } from "./client.ts";
import { getProblemQuery } from "./queries.ts";

export interface Problem {
  difficulty: "Easy" | "Medium" | "Hard";
  questionId: string;
  title: string;
  titleSlug: string;
  content: string;
  isPaidOnly: boolean;
  exampleTestcases: string;
  codeSnippets: CodeSnippetsEntity[];
  stats: string;
  solution: Solution;
  status: string;
  sampleTestCase: string;
  metaData: string;
  envInfo: string;
}

interface GetProblemBySlugResponse {
  problem: Problem;
}

interface CodeSnippetsEntity {
  lang: string;
  langSlug: string;
  code: string;
}

interface Solution {
  id: string;
  canSeeDetail: boolean;
  paidOnly: boolean;
  hasVideoSolution: boolean;
  paidOnlyVideo: boolean;
}

export const getProblemBySlug = (slug: string): Promise<Problem | null> =>
  client
    .post("/graphql", getProblemQuery(slug))
    .then((response) => response.data.data.question || null)
    .catch(console.log);
