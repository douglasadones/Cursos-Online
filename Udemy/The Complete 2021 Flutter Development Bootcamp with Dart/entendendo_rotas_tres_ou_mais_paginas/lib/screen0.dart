import 'package:flutter/material.dart';
import 'screen1.dart';
import 'screen2.dart';

class Screen0 extends StatelessWidget {
  const Screen0({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.purple,
          title: const Center(
            child: Text('Screen 0'),
          ),
        ),
        body: Center(
          child: Column(
            children: [
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(context, '/first');
                      },
                      style: ElevatedButton.styleFrom(primary: Colors.red),
                      child: const Text('Go To Screen 1'),
                    ),
                    const SizedBox(height: 5.0),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(context, '/second');
                      },
                      style: ElevatedButton.styleFrom(primary: Colors.blue),
                      child: const Text('Go To Screen 2'),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ));
  }
}
