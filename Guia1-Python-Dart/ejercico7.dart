void main() {
  List<dynamic> lista = ["a", 2, 0, "b", 8, "c"];

  List<int> numeros = [];

  for (var elemento in lista) {
    if (elemento is int) {
      numeros.add(elemento);
    }
  }

  print(numeros);
}
