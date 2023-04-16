
#define small   1
#define normal  2
#define big     3
#define large   4

#define cls(x,y,w,h) tft.fillRect(x,y,w,h,black);

void texts(char*text, char* sizes, char* color, int x, int y)
{
  tft.setCursor(x, y);
  tft.setTextSize(sizes);
  tft.setTextColor(color);
  tft.print(text);
}


#define black       0x0000      /*   0,   0,   0 */
#define navy        0x000F      /*   0,   0, 128 */
#define darkgreen   0x03E0      /*   0, 128,   0 */
#define darkcyan    0x03EF      /*   0, 128, 128 */
#define maroon      0x7800      /* 128,   0,   0 */
#define purple      0x780F      /* 128,   0, 128 */
#define olive       0x7BE0      /* 128, 128,   0 */
#define lightgrey   0xC618      /* 192, 192, 192 */
#define darkgrey    0x7BEF      /* 128, 128, 128 */
#define blue        0x001F      /*   0,   0, 255 */
#define green       0x07E0      /*   0, 255,   0 */
#define cyan        0x07FF      /*   0, 255, 255 */
#define red         0xF800      /* 255,   0,   0 */
#define magenta     0xF81F      /* 255,   0, 255 */
#define yellow      0xFFE0      /* 255, 255,   0 */
#define white       0xFFFF      /* 255, 255, 255 */
#define orange      0xFDA0      /* 255, 180,   0 */
#define greenyellow 0xB7E0      /* 180, 255,   0 */
#define pink        0xFC9F
