MAIN=main.py
MATH_LIB=math_lib.py
MATH_TESTS=math_lib_tests.py
PROFILING=profiling.py
REQUIREMENTS=requirements.txt
ZIP=xbella01_xmatus35_xvrabl05

.PHONY:
	all
	pack
	test
	doc
	clean
	run
	profile
all: requirements run
	
requirements:
	python3 -m pip install -r $(REQUIREMENTS)

pack: doc installer clean
	mkdir -p ../../$(ZIP)/repo

	cp -r ../ ../../$(ZIP)/repo
#	mv ../../$(ZIP)/repo/installer ../../$(ZIP)
	mv ../../$(ZIP)/repo/doc ../../$(ZIP)
	
	cd ../../ && zip -r $(ZIP).zip $(ZIP)
	rm -rf ../../$(ZIP)

clean:
	rm -rf __pycache__	
#TODO
test: $(MATH_TESTS)
	python3 -m pytest $(MATH_TESTS)

doc: Doxyfile
	doxygen Doxyfile

run: $(MAIN)
	python3 $(MAIN)

profile: $(PROFILING)
	python3 $(PROFILING) > ../profiling/vystup.txt

installer:
#TODO
