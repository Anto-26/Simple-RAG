const fileInput = document.getElementById("fileInput");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");

const questionInput = document.getElementById("questionInput");
const askBtn = document.getElementById("askBtn");
const answerEl = document.getElementById("answer");

uploadBtn.addEventListener("click", async () => {
  const file = fileInput.files[0];
  if (!file) {
    uploadStatus.textContent = "Please choose a file first.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  uploadBtn.disabled = true;
  uploadStatus.textContent = "Processing...";

  try {
    const response = await fetch("/api/upload", { method: "POST", body: formData });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Upload failed");
    }

    uploadStatus.textContent = `Processed "${data.filename}" into ${data.chunks} chunks.`;
    questionInput.disabled = false;
    askBtn.disabled = false;
  } catch (err) {
    uploadStatus.textContent = `Error: ${err.message}`;
  } finally {
    uploadBtn.disabled = false;
  }
});

askBtn.addEventListener("click", async () => {
  const question = questionInput.value.trim();
  if (!question) {
    return;
  }

  askBtn.disabled = true;
  answerEl.textContent = "Thinking...";

  try {
    const formData = new FormData();
    formData.append("question", question);

    const response = await fetch("/api/ask", { method: "POST", body: formData });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Request failed");
    }

    answerEl.textContent = data.answer;
  } catch (err) {
    answerEl.textContent = `Error: ${err.message}`;
  } finally {
    askBtn.disabled = false;
  }
});

questionInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    askBtn.click();
  }
});
