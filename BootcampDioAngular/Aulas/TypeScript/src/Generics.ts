//generics
function concatArray<T>(...itens: T[]): T[] {
    return new Array().concat(...itens);
  }
  
  const numArray = concatArray<number[]>([1, 5], [3]);
  const stgArray = concatArray<string[]>(["felipe", "goku"], ["vegeta"]);
  
  console.log(numArray);
  console.log(stgArray);

  /*generics serve para você passar o tipo depois, inserindo o T como tipo no momento, mas qunado for chamdo foi passaro o tipo desejado*/