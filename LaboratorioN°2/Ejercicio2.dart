import 'dart:math';

void main() {
  List<int> primeralista = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];
  List<int> segundalista = [];

  Random random = Random();
  for (int i = 0; i < 10; i++) {
    int numAleatorio = random.nextInt(5) + 1;
    segundalista.add(-numAleatorio);
  }
  print("Primera lista: $primeralista");
  print("Segunda lista: $segundalista");
}
