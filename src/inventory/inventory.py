



'''
++++++++++++++++++++++++++++++++++++++++++++

make a "calendar" with how much available items we have in each period

in it I need to have defined periods from one relevant date to an other...
like:

today - next event start, an other level start, the end of the first one, the end of the seecond one, an other...... the end of the last one, the end

- first, organice all events (no mater its place)
- a method that takes a date and search for the next relevant date, each time an event is checked from start to end it jumps into the next one
- end up with a list of concatenated intervales with how much items are available in each period
- for creating an event its period must be compared to the group of intervals it overlap...
  - run though the inventary periods, 
  - once it gets into an interval, save them till the next dont overlap
  - brake
  - take the minimun available value of each item
  - 


'''