import express from 'express';
import cors from 'cors';
import { spawn } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

// Recreate __dirname in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

app.post('/compute', (req, res) => {
  const { start, end } = req.body;

  const pythonProcess = spawn('python', ['app.py', start, end], {
    cwd: __dirname // now correctly set
  });

  let result = '';

  pythonProcess.stdout.on('data', (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on('data', (err) => {
    console.error(`Python error: ${err}`);
  });

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      return res.status(500).json({ error: "Python script failed" });
    }
    res.json({ result: result.trim() });
  });
});

app.listen(5000, () => {
  console.log("Server running on http://localhost:5000");
});
