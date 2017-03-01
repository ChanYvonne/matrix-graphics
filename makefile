run: 	main.py
	python matrix.py
	python main.py
	convert pic.ppm img.png
	rm -rf pic.ppm

clean:
	rm *.pyc
	rm *~
