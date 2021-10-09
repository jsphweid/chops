import { client } from "./client.ts";
import { getTopDiscussionTitlesQuery } from "./queries.ts";

export const getTopDiscussionTitles = (questionId: string): Promise<string[]> =>
  client
    .post("/graphql", getTopDiscussionTitlesQuery(questionId))
    .then((response) =>
      response.data.data.questionTopicsList.edges.map((e: any) => e.node.title)
    )
    .catch(console.error);

const wait = () => new Promise((resolve) => setTimeout(resolve, 1000));
