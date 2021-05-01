  #include <ESP8266WiFi.h>
  #include <BlynkSimpleEsp8266.h>
  #define relay D1
  #define triggerPin  D8
  #define echoPin     D7
  #define BLYNK_PRINT Serial
  
  // masukkan Auth Token dari Blynk App
  const char* auth = "SXKRugzRqRUVfKbw1vSpyNycLwrT_q2J";
   
  // koneksi wifi beserta password
  const char* ssid="Shalma";
  const char* password="b4n9t4n_136";
   
  int lampuNyala = LOW;
  int lampuMati = HIGH;
  long jarak, duration;
  bool keadaan= 0;
  char perintah;
  
  void setup() {
    Serial.begin(9600);
    pinMode(relay, OUTPUT);
    pinMode(triggerPin, OUTPUT);
    pinMode(echoPin, INPUT);
    digitalWrite(relay, lampuMati);
    Blynk.begin(auth, ssid, password);
  }
  
  void loop() {  
    Blynk.run();
  
    digitalWrite(triggerPin, LOW);
    delayMicroseconds(2);
  
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(10);
  
    digitalWrite(triggerPin, LOW);
  
    duration = pulseIn(echoPin, HIGH);
    jarak = (duration/2) / 29.1;
  
    

    if(jarak < 15){
      if(keadaan==0){
        digitalWrite(relay, lampuNyala); keadaan = 1;
        
        }
      else{ 
        digitalWrite(relay, lampuMati); keadaan = 0; 
        
        }
    delay(1000);
    }
    Serial.print("keadaan lampu : ");
    Serial.println(keadaan);
//    Serial.print("jarak : ") ;
//    Serial.println(jarak);
  }
//if (Serial.available() > 0) 
  //{
  //perintah = Serial.read();
  //if (perintah == ('A')){
    //digitalWrite(relay, lampuNyala);
    //Serial.print("A – ");
    //Serial.println("Lampu Nyala");
  //}
  //else if (perintah == ('B')){
    //digitalWrite(relay, lampuMati);
    //Serial.print("B – ");
    //Serial.println("Lampu Mati");
  //}
//}
