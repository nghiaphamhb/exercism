export function decodedResistorValue(colors: string[]): string {
  const first = COLORS.indexOf(colors[0]);
  const second = COLORS.indexOf(colors[1]);
  const multiple = 10 ** COLORS.indexOf(colors[2])
  const result = (first * 10 + second) * multiple;

  if(result >= 1_000_000_000) {
    return result / 1_000_000_000 + ' gigaohms';
  }
  if(result >= 1_000_000) {
    return result / 1_000_000 + ' megaohms';
  }
  if(result >= 1_000) {
    return result / 1_000 + ' kiloohms';
  }

  return result + ' ohms';
}

export const COLORS: string[] = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
]