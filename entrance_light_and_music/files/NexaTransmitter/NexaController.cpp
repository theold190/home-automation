#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include "NexaTransmitter.h"

static void show_usage(std::string name)
{
    std::cerr << "Usage: " << name << " <option(s)> on/off"
              << "Options:\n"
              << "\t--pin\t\tPin number with RF transmitter according to WiringPI numbering\n"
              << "\t--unit\t\tUnit number\n"
              << "\t--remote-id\tRemote id\n"
              << std::endl;
}

// See http://wiringpi.com/pins/ for info about pins used by wiringpi
const int PRIO = 55;

bool setup() {
    if(wiringPiSetup() == -1) {
        return false;
    }

    // Set a custom priority of the program in order to increase timing
    (void)piHiPri(PRIO);
    return true;
}

int main(int argc, char* argv[]) {
    short pin = -1;
    short unit = -1;
    bool on = false;
    unsigned long remote_id = 0;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--pin") {
            if (i + 1 < argc) { // Make sure we aren't at the end of argv!
                pin = std::stoi(std::string(argv[++i]));
            } else {
                printf("--pin option requires one argument.");
                return 1;
            }
        } else if (arg == "--unit") {
            if (i + 1 < argc) { // Make sure we aren't at the end of argv!
                unit = std::stoi(std::string(argv[++i]));
            } else {
                printf("--unit option requires one argument.");
                return 1;
            }
        } else if (arg == "--remote-id") {
            if (i + 1 < argc) { // Make sure we aren't at the end of argv!
                remote_id = std::stoi(std::string(argv[++i]));
            } else {
                printf("--remote_id option requires one argument.");
                return 1;
            }
        } else if ((arg == "on") || (arg == "off")) {
            on = (arg == "on");
        }
    }
    std::cout << "pin: " << pin << ", unit: " << unit << ", remote id: " << remote_id << std::endl;
    if ((pin < 0) || (unit < 0) || (remote_id < 0)) {
        printf("Some required parameters were not provided\n");
        show_usage(argv[0]);
        return 1;
    }
    if(!setup()) {
        return EXIT_FAILURE;
    }

    NexaTransmitter remote(pin, remote_id);
    printf("Turning %s unit %d\n", (on ? "on": "off"), unit);
    remote.setSwitch(on, unit);
    return EXIT_SUCCESS;
}
