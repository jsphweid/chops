export namespace Datetime {
  export function getMinutesBetween(date1: Date, date2: Date): number {
    return Math.round(Math.abs(date1.getTime() - date2.getTime()) / 60000);
  }
}
