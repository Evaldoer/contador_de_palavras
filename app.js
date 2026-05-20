const stopwords = new Set(["de", "a", "o", "e", "do", "da", "em", "um", "uma", "para", "com"]);

const textInput = document.querySelector("#textInput");
const wordTotal = document.querySelector("#wordTotal");
const wordList = document.querySelector("#wordList");
const countButton = document.querySelector("#countButton");
const clearButton = document.querySelector("#clearButton");

const firstNumber = document.querySelector("#firstNumber");
const secondNumber = document.querySelector("#secondNumber");
const operation = document.querySelector("#operation");
const calcResult = document.querySelector("#calcResult");
const calculateButton = document.querySelector("#calculateButton");

function countWords() {
  const words = textInput.value
    .toLowerCase()
    .match(/\b[\p{L}\p{N}_]+\b/gu) || [];
  const filteredWords = words.filter((word) => !stopwords.has(word));
  const frequency = new Map();

  filteredWords.forEach((word) => {
    frequency.set(word, (frequency.get(word) || 0) + 1);
  });

  const topWords = [...frequency.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, 10);

  wordTotal.textContent = `${filteredWords.length} palavra${filteredWords.length === 1 ? "" : "s"}`;
  wordList.innerHTML = "";

  if (topWords.length === 0) {
    const item = document.createElement("li");
    item.textContent = "Nenhuma palavra para exibir.";
    wordList.appendChild(item);
    return;
  }

  topWords.forEach(([word, total]) => {
    const item = document.createElement("li");
    item.textContent = `${word}: ${total}`;
    wordList.appendChild(item);
  });
}

function calculate() {
  const left = Number(firstNumber.value);
  const right = Number(secondNumber.value);
  let result = 0;

  if (!Number.isFinite(left) || !Number.isFinite(right)) {
    calcResult.textContent = "Informe numeros validos";
    return;
  }

  if (operation.value === "+") result = left + right;
  if (operation.value === "-") result = left - right;
  if (operation.value === "*") result = left * right;
  if (operation.value === "/") {
    if (right === 0) {
      calcResult.textContent = "Divisao por zero";
      return;
    }
    result = left / right;
  }

  calcResult.textContent = `Resultado: ${Number(result.toFixed(6))}`;
}

function parseCsv(csv) {
  const [headerLine, ...rows] = csv.trim().split(/\r?\n/);
  const headers = headerLine.split(",").map((header) => header.trim());

  return rows.map((row) => {
    const values = row.split(",");
    return Object.fromEntries(headers.map((header, index) => [header, Number(values[index])]));
  });
}

function mean(values) {
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function median(values) {
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
}

function sampleStd(values) {
  if (values.length < 2) return 0;
  const average = mean(values);
  const variance = values.reduce((sum, value) => sum + (value - average) ** 2, 0) / (values.length - 1);
  return Math.sqrt(variance);
}

function drawScatter(data) {
  const canvas = document.querySelector("#scatterChart");
  const ctx = canvas.getContext("2d");
  const padding = 42;
  const xs = data.map((item) => item.col1);
  const ys = data.map((item) => item.col2);
  const minX = Math.min(...xs);
  const maxX = Math.max(...xs);
  const minY = Math.min(...ys);
  const maxY = Math.max(...ys);
  const width = canvas.width;
  const height = canvas.height;

  ctx.clearRect(0, 0, width, height);
  ctx.strokeStyle = "#dce2dd";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(padding, padding);
  ctx.lineTo(padding, height - padding);
  ctx.lineTo(width - padding, height - padding);
  ctx.stroke();

  ctx.fillStyle = "#66706b";
  ctx.font = "14px Arial";
  ctx.fillText("col2", 12, 24);
  ctx.fillText("col1", width - 72, height - 12);

  data.forEach((point) => {
    const x = padding + ((point.col1 - minX) / (maxX - minX || 1)) * (width - padding * 2);
    const y = height - padding - ((point.col2 - minY) / (maxY - minY || 1)) * (height - padding * 2);

    ctx.beginPath();
    ctx.fillStyle = "#0f766e";
    ctx.arc(x, y, 6, 0, Math.PI * 2);
    ctx.fill();
  });
}

async function loadCsvStats() {
  try {
    const response = await fetch("dados.csv");
    const data = parseCsv(await response.text());
    const col1 = data.map((item) => item.col1).filter(Number.isFinite);

    document.querySelector("#meanValue").textContent = mean(col1).toFixed(2);
    document.querySelector("#medianValue").textContent = median(col1).toFixed(2);
    document.querySelector("#stdValue").textContent = sampleStd(col1).toFixed(2);
    drawScatter(data);
  } catch (error) {
    document.querySelector("#meanValue").textContent = "Erro";
    document.querySelector("#medianValue").textContent = "Erro";
    document.querySelector("#stdValue").textContent = "Erro";
  }
}

countButton.addEventListener("click", countWords);
clearButton.addEventListener("click", () => {
  textInput.value = "";
  countWords();
});
calculateButton.addEventListener("click", calculate);

countWords();
calculate();
loadCsvStats();
