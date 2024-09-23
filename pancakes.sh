#!/bin/bash

# Function to decode the challenge
decode_challenge() {
    local challenge_string=$1
    local iterations=$2
    # Decode the challenge iterations+1 times
    for ((i=0; i<=iterations; i++)); do
        challenge_string=$(echo "$challenge_string" | base64 -d)
    done
    echo "$challenge_string"
}

# Connect to the server
nc chal.pctf.competitivecyber.club 9001 | while read line; do
    # Find the line that starts with "Challenge:"
    if [[ "$line" =~ Challenge:\ (.+) ]]; then
        # Extract the encoded challenge and iteration count (current step)
        encoded_challenge=$(echo "$line" | cut -d ' ' -f 2 | cut -d '|' -f 1)
        current_iteration=$(echo "$line" | cut -d '|' -f 2 | cut -d '(' -f 1)
        # Decode the challenge using the helper function
        decoded=$(decode_challenge "$encoded_challenge" "$current_iteration")
        # Send the decoded challenge back with the current iteration
        echo "$decoded|$current_iteration"
    fi
done
