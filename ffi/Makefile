#
# GPLv2
P = substring
CFLAGS_STD = -g -Wall -O3 -march=native -Wno-deprecated -Wno-parentheses -Wno-format

CFLAGS_EXTRA =  -std=c11 -Wall -Wshadow -Wpointer-arith -Wcast-qual -Wstrict-prototypes -Wmissing-prototypes
CFLAGS = $(CFLAGS_STD) $(CFLAGS_EXTRA) $(CFLAGS_LIB)

bin: $(P) 

OBJECTS: substring.o



clean:
	@echo "Cleaning..."
	rm -rf *.o *.d $(P) tests/output/*

test: run-tests.sh $(P)
	./run-tests.sh

.PHONY: clean

ifneq "$(MAKECMDGOALS)" "clean"
-include ${SOURCES:.c=.d}
-include ${T_SOURCES:.c=.d}
endif
