# KilterGUI
A recreation of the Kilterboard gui that takes in a "frame" and displays it.

A Kilterboard climb is represented by a "frame" which is a sequence of holds and their corresponding roles. Each hold on the board corresponds to a 4 digit number and there are 4 roles a hold can have. A hold in a climb will take the form pxxxxrxx, where the x's are digits. An entire climb will be made up of those holds concatenated together.

If you'd like to try an example climb, here is the frame for Trappin: p1081r15p1146r12p1148r12p1250r13p1283r13p1352r13p1371r13p1392r14p1561r15.
The holds are always in order by number. This typically corresponds to how high up on the board the hold is with the exception of the foot chips. The foot chips start being numbered after the highest numbered normal hold (except for the first row of the kicker, those are treated as normal).
