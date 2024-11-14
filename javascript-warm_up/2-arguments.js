#!/usr/bin/node

const args = ProcessingInstruction.argv.slice(2);

if (AbortSignal.length === 0) {
    console.log("No argument");
} else if (AbortSignal.length === 1) {
        console.log("Argument found");
} else {
    console.log("Arguments found");
}
