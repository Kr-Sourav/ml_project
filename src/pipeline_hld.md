graph TD
  subgraph Offline World (Batch Processing - Daily/Weekly)
      A1(HDFS: GPS Logs) --> B(Spark Job: Data Processing);
      A2(HDFS: Trip Logs) --> B;
      B -- "Map-matching, Labeling, Feature Engineering" --> C{Offline Feature Store};
      C -- "Historical Features" --> D[Spark Job: Model Training];
      B -- "Training Data" --> D;
      D -- "Trained Model Artifact" --> E[Model Registry];
  end

  subgraph Real-time World (Stream Processing)
      F(Kafka: Live GPS Stream) --> G[Flink/Spark Streaming Job];
      G -- "Aggregate real-time speeds, counts per segment/H3" --> H{Online Feature Store (Redis)};
  end

  subgraph Online Serving World (Low Latency)
      I(Client App) --> J[API Gateway / Load Balancer];
      J -- "1MM QPS" --> K(Prediction Service);
      K -- "1. Decompose route into segments" --> K;
      K -- "2. Batch Fetch Features for all segments" --> L{Feature Store Gateway};
      L --> H;
      L --> C;
      H --> L;
      C --> L;
      L -- "Historical & Real-time Features" --> K;
      E -- "Load latest model" --> M[Model Serving Engine (Triton)];
      K -- "3. Batch Predict on Features" --> M;
      M -- "Per-segment predictions" --> K;
      K -- "4. Aggregate & Return ETA" --> J;
      J --> I;
  end

  subgraph Monitoring & MLOps
      K -- "Logs & Metrics" --> O(Prometheus & Grafana);
      M -- "Inference Metrics" --> O;
      P(Evaluation Pipeline) -- "Compares model in Registry vs. Production" --> Q(Alerting/Deployment);
      E --> P;
      A2 -- "Ground Truth" --> P;
      K -- "Prediction Logs" --> P;
  end
