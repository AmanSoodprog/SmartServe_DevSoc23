# import tensorflow as tf
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# #from tensorflow.keras import regularizers

# data = pd.read_csv("C:/Users/sooda/Desktop/DataUse.csv")

# features = data[["screen_size", "4g", "5g", "rear_camera_mp", "front_camera_mp",
#                  "internal_memory", "ram", "battery", "weight", "release_year", "days_used","normalized_new_price"]].values
# target = data["normalized_used_price"].values
# target = np.expand_dims(target, axis=1)

# # features = np.asarray(features).astype(np.float32)
# # tf.keras.utils.normalize(features)
# # tf.keras.utils.normalize(target)

# split_index = int(0.8 * len(features))
# train_features = features[:split_index]
# train_target = target[:split_index]
# test_features = features[split_index:]
# test_target = target[split_index:]


# scaler = MinMaxScaler()
# train_features_scaled = scaler.fit_transform(train_features)
# test_features_scaled = scaler.fit_transform(test_features)
# test_target_scaled = scaler.fit_transform(test_target)
# train_target_scaled = scaler.fit_transform(train_target)


# model = tf.keras.models.Sequential([
#     # tf.keras.layers.Dense(8192, activation='relu', input_shape=(12,)),
#     # tf.keras.layers.Dense(4096, activation='relu'),
#     # tf.keras.layers.Dense(2048, activation='relu', input_shape=(12,)),
#     #  tf.keras.layers.Dense(2048, activation='relu', input_shape=(12,), kernel_regularizer=regularizers.l2(0.01)),
#     # # tf.keras.layers.Dense(2048, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
#     # tf.keras.layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
#     # tf.keras.layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
#     # tf.keras.layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
#     # tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
#     tf.keras.layers.Dense(64, activation='relu',input_shape=(12,)),
#     tf.keras.layers.Dense(32, activation='relu'),
#     tf.keras.layers.Dense(16, activation='relu'),
#     tf.keras.layers.Dense(8, activation='relu'),
#     tf.keras.layers.Dense(1)
# ])


# #optimizer = tf.keras.optimizers.Adam(learning_rate=0.001,clipvalue=1.0)
# #model.compile(optimizer=optimizer, loss='mean_absolute_error')
# #model.fit(train_features_scaled, train_target_scaled, epochs=5, batch_size=32)

# model.compile(optimizer='adam', loss='mean_squared_error')
# model.fit(train_features_scaled, train_target_scaled, epochs=50, batch_size=32)

# #  6: Evaluate the model
# loss = model.evaluate(test_features_scaled, test_target_scaled)
# print("Mean squared error: ", loss)

# # model.save("DeviceModel.h5")

# loaded_model = tf.keras.models.load_model('C:/Users/sooda/Desktop/DeviceModel.h5')

# #single_input = np.array([[6.4, 1, 1, 12, 8, 128, 4, 4000, 180, 2022, 365, 0.8]])  # Example input values

# #single_input_scaled = scaler.fit_transform(single_input)

# #   Get the prediction
# #predicted_used_price_scaled = loaded_model.predict(single_input)
# #predicted_used_price = scaler.inverse_transform(predicted_used_price_scaled)

# #print("Predicted used price:", predicted_used_price_scaled)


# #  Make predictions
# new_data = pd.read_csv("C:/Users/sooda/Desktop/DataUse.csv")
# new_features = new_data[["screen_size", "4g", "5g", "rear_camera_mp", "front_camera_mp",
#                          "internal_memory", "ram", "battery", "weight", "release_year", "days_used","normalized_new_price"]].values

# new_features_scaled= scaler.fit_transform(new_features)

# predicted_used_prices = model.predict(new_features_scaled)
# print("Predicted used prices:", predicted_used_prices)
