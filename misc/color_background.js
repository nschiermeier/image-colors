/* colorBG
 * A function that automatically colors cells in Google Sheets with the
 * hex codes given in the cell.
*/

function colorBG() {
  // Get the all of the hex codes
  var colors = SpreadsheetApp.getActiveSheet().getRange("B2:B866").getValues();

  for (let i = 0; i < colors.length; i++) {
    // Change the background of each cell to it's specified color
    var cell = SpreadsheetApp.getActiveSheet().getRange("B2:B866").getCell(i+1, 1)
    cell.setBackground(colors[i])
  }
}
