int OutPin = A0; // Lưu chân ra của cảm biến
void setup() 
{
  //Đối với một chân analog bạn không cần pinMode
  Serial.begin(9600);//Mở cổng Serial ở mức 9600
  pinMode (7, INPUT_PULLUP);
  pinMode (13, OUTPUT);
}

void loop() 
{
  int value = analogRead(OutPin);     // Ta sẽ đọc giá trị hiệu điện thế của cảm biến
                                      // Giá trị được số hóa thành 1 số nguyên có giá trị
                                      // trong khoảng từ 0 đến 1023
  Serial.println(value);//Xuất ra serial Monitor. Nhấn Ctrl+Shift+M để xem                                     
  delay(10);
  //if (digitalRead (7) == 0)
  if (value > 600)
  {
   digitalWrite (13, HIGH);
  }
  else
  digitalWrite (13, LOW);
}
