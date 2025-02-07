function apenasMobile() {
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;
  
    // Verifica se é um dispositivo móvel
    if (/Mobi|Android|iPhone|iPad|iPod|Opera Mini/i.test(userAgent)) {
      console.log("Você está acessando de um dispositivo móvel.");
    } else {
      alert("Esta aplicação só pode ser acessada em dispositivos móveis.");
      window.location.href = "https://www.seusite.com/aviso";
    }
  }
  
  apenasMobile();
  