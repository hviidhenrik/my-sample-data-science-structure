model_cfg = {
    "high_level_parameters": {  # parameters common to all models, e.g. how much data to get, debugging parameters etc.
        "data_period": ("2020-01-01", "2023-01-01"),
        "parameter2": 60,
        "parameter3": 20,
    },
    "low_level_parameters": {
        "model1_parameters": {
            "learning_rate": 1,
            "hidden_layers": 2,
        },
        "model2_parameters": {
            "ewma_alpha": 0.05,
            "sigma": 3,
        },
    },
}