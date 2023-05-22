import 'dart:math';

void main() {
  List<int> a = [4, 3, 2, 2, 1];
  List<int> b = [-3, 2, 8, 0, 1];

  List<int> resultado = List.generate(a.length, (i) => a[i] * b[i]);

  List<int> nuevalista = List.generate(5, (_) => Random().nextInt(5) - 5);

  List<int> listafinal = [...resultado, ...nuevalista];
  listafinal.sort((a, b) => b.compareTo(a));

  print(listafinal);
}
