function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteActivity(activityId) {
  fetch("/deleteActivity", {
    method: "POST",
    body: JSON.stringify({ activityId: activityId }),
  }).then((_res) => {
    window.location.href = "/activities";
  });
}

function CompletedActivity(activityId){
  fetch("/CompletedActivity", {
    method: "POST",
    body: JSON.stringify({ activityId: activityId }),
  }).then((_res) => {
    window.location.href = "/activities";
  });
}
