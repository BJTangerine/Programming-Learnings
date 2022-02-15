// Function to find the number of points that will cause a bust
def pointsToBust(hand: Int) = {
  // If the hand is a bust, 0 points remain
  if (bust(hand))
    println(0)
  // Else difference is calculated between 21 and the current hand
  else
    println(21 - hand)
}

// Sample list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loops through hands, finding each hand's number of points to bust
hands.foreach(pointsToBust)