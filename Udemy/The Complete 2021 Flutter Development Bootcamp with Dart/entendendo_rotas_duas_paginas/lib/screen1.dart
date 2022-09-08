import 'package:flutter/material.dart';
import 'screen2.dart';

class Screen1 extends StatelessWidget {
  const Screen1({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.red,
        title: const Center(
          child: Text('Screen 1'),
        ),
      ),
      body: Center(
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(primary: Colors.red),
          onPressed: () {
            Navigator.push(
              // Muda para a página informada
              context,
              MaterialPageRoute(
                builder: (context) {
                  return const Screen2();
                },
              ),
            );
          },
          child: const Text('Go Forwards To Screen 2'),
        ),
      ),
    );
  }
}
