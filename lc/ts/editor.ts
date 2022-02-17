import { Utils } from "./utils.ts";
export namespace Editor {
  export const openInSublime = (file: string): Promise<void> =>
    Utils.runCommand(["code", file]);

  export const openInTextEdit = (file: string): Promise<void> =>
    Utils.runCommand(["open", "-a", "TextEdit", file]);

  export const openInRandomTextEditor = (file: string): Promise<void> =>
    Math.random() < 0.96 ? openInSublime(file) : openInTextEdit(file);
}
