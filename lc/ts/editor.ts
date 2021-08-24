export namespace Editor {
  const runCommand = async (command: string[]): Promise<void> => {
    const p = Deno.run({
      cmd: command,
      stdout: "piped",
      stderr: "piped",
    });

    await p.status();
    return;
  };

  export const openInSublime = (file: string): Promise<void> =>
    runCommand(["subl", file]);

  export const openInTextEdit = (file: string): Promise<void> =>
    runCommand(["open", "-a", "TextEdit", file]);
}
