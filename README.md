# ❤️ Heart Disease Prediction System

**Live Demo**: https://heart-disease-predictor-k2l2.onrender.com/

Developed a Heart Disease Prediction System using K-Nearest Neighbors (KNN) and Streamlit. Implemented data preprocessing, feature scaling, model training, and real-time prediction with an interactive web interface, achieving a 90.2% accuracy and 91.3% F1 score.

A Streamlit application that uses a K-Nearest Neighbors model to estimate heart
disease risk from patient health measurements.

> This project is for educational use only. It is not a medical device and must
> not be used as a substitute for professional diagnosis or treatment.

## Methodology and Results

**Dataset**: 
The model is trained on the [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction), containing 918 observations and 11 clinical features. A local copy is included in `data/heart.csv` for reproducibility.

**Preprocessing & Model Selection**:
- Categorical variables were one-hot encoded (dropping the first category).
- Continuous variables were scaled using `StandardScaler`.
- A **K-Nearest Neighbors (KNN)** classifier was selected for its simplicity and interpretability on scaled tabular data. 
- Using 5-fold cross-validation on an 80% training split, hyperparameter tuning identified $k=9$ as the optimal number of neighbors.

**Evaluation Metrics (on 20% hold-out test set)**:
- **Accuracy**: 90.2%
- **Precision**: 90.4%
- **Recall**: 92.2%
- **F1 Score**: 91.3%

**Confusion Matrix**:
```
[[72, 10],
 [ 8, 94]]
```

## Run locally

Use Python 3.11 so the runtime matches production:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

The app is available at `http://localhost:8501`.

## Deploy to Render

The repository includes a Docker image and a Render Blueprint:

1. Push this repository to GitHub.
2. Sign in to [Render](https://dashboard.render.com/).
3. Select **New > Blueprint** and connect this repository.
4. Confirm the `heart-disease-predictor` service and apply the Blueprint.
5. Wait for the health check at `/_stcore/health` to pass.

Render will build the `Dockerfile`, publish the app over HTTPS, and redeploy it
after each commit to the connected branch.

The Blueprint starts on Render's free plan to avoid an unexpected charge. Free
services may sleep when idle. Before serving real traffic, upgrade the service
to a paid instance and configure uptime alerts and a custom domain in Render.

*(Note: Because this is deployed on a free tier, the app will spin down after a period of inactivity. The first request after a period of inactivity may take 30-60 seconds to load. Please be patient!)*

## Run with Docker

```bash
docker build -t heart-disease-predictor .
docker run --rm -p 8501:10000 heart-disease-predictor
```

Open `http://localhost:8501`. The container health endpoint is
`http://localhost:8501/_stcore/health`.

## Production files

- `Dockerfile`: reproducible Python 3.11 image running as a non-root user
- `render.yaml`: Render web service and health-check configuration
- `.dockerignore`: excludes local and sensitive files from the image
- `.streamlit/config.toml`: disables telemetry and enables headless mode
- `requirements.txt`: pinned runtime dependencies
