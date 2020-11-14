all: NexaExample NexaController

NexaExample: NexaTransmitter.o NexaExample.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi

NexaController: NexaTransmitter.o NexaController.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi

clean:
	$(RM) *.o NexaTransmitter NexaExample
