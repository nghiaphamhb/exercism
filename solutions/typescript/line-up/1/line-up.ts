export function format(name: string, number: number): string {
  let rank: string;
  const lastDigit = number % 10;
  const twoLastDigit = number % 100;
  if (twoLastDigit >= 11 && twoLastDigit <= 13) { // 11, 12, 13
     rank = number + 'th';
  } else if(lastDigit === 1) {
    rank = number + 'st';
  } else if (lastDigit === 2) {
    rank = number + 'nd';
  } else if (lastDigit === 3) {
    rank = number + 'rd';
  } else {
    rank = number + 'th';
  }

  return name + ', you are the ' + rank + ' customer we serve today. Thank you!';
}
