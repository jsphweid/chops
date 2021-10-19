import { client } from "./client.ts";
import { getTopDiscussionTitlesQuery } from "./queries.ts";

export const getTopDiscussionTitles = (problemId: string): Promise<string[]> =>
  client
    .post("/graphql", getTopDiscussionTitlesQuery(problemId))
    .then((response) =>
      response.data.data.problemTopicsList.edges.map((e: any) => e.node.title)
    )
    .catch(console.error);

const wait = () => new Promise((resolve) => setTimeout(resolve, 1000));
