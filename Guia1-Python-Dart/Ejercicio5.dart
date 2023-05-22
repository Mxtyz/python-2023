import 'dart:math';

void main() {
  List<List<int>> listas = List.generate(3, (_) => listaaleatoria(7, 30, 100));

  List<double> promedios = listas.map((lista) => promedio(lista)).toList();

  print(promedios);
}

List<int> listaaleatoria(int longitud, int min, int max) {
  Random random = Random();
  return List<int>.generate(
      longitud, (_) => random.nextInt(max - min + 1) + min);
}

double promedio(List<int> lista) {
  double suma = lista.reduce((a, b) => a + b).toDouble();
  return suma / lista.length;
}
