export function toRna(dna: string): string {
  let rna: string = ''; // immutable string 
  const complement = new Map<string, string>([
    ['G', 'C'],
    ['C', 'G'],
    ['T', 'A'],
    ['A', 'U'],
  ]);

  for(const c of dna){
    const value = complement.get(c);
    if (complement.get(c) == undefined) {
      throw new Error('Invalid input DNA.')
    }
    rna += value;
  }
  return rna;
}
