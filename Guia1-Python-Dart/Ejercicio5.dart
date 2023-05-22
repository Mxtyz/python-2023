import 'dart:math';

void main() {
  List<List<int>> listas =
      List.generate(3, (_) => generarListaAleatoria(7, 30, 100));

  List<double> promedios =
      listas.map((lista) => calcularPromedio(lista)).toList();

  print(promedios);
}

List<int> generarListaAleatoria(int longitud, int min, int max) {
  Random random = Random();
  return List<int>.generate(
      longitud, (_) => random.nextInt(max - min + 1) + min);
}

double calcularPromedio(List<int> lista) {
  double suma = lista.reduce((a, b) => a + b).toDouble();
  return suma / lista.length;
}
