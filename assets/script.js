fetch("kalender/kalender.ics", { method: "HEAD" })
  .then(res => {
    document.getElementById("status").innerText =
      "Kalender erreichbar – letzter Sync OK";
  })
  .catch(() => {
    document.getElementById("status").innerText =
      "Fehler beim Kalender";
  });
