import { Utils } from "./utils.ts";
import * as RawRequests from "./leetcode-service/raw-requests/index.ts";

export namespace Difficulty {
  export enum Type {
    Easy,
    Medium,
    Hard,
  }

  export const when =
    <T>(when: { easy: () => T; medium: () => T; hard: () => T }) =>
    (difficulty: Type): T => {
      switch (difficulty) {
        case Type.Easy:
          return when.easy();
        case Type.Medium:
          return when.medium();
        case Type.Hard:
          return when.hard();
        default:
          throw new Error("Not handled.");
      }
    };

  export const fromCliArgs = (strings: string[]): Type | null =>
    Utils.fromCliArgs(
      {
        easy: Type.Easy,
        medium: Type.Medium,
        hard: Type.Hard,
      },
      strings
    );

  export const toLeetcodeName: (difficulty: Type) => RawRequests.Difficulty =
    when({
      easy: () => "EASY",
      medium: () => "MEDIUM",
      hard: () => "HARD",
    });
}
