import tensorflow as tf

class PromoModel:
    def __init__(self, input_shape=(64, 64, 3), output_shape=10):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=self.input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.output_shape, activation='softmax')  # For classification tasks
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def predict_layout(self, inputs):
        return self.model.predict(inputs)

    def load_weights(self, path):
        self.model.load_weights(path)
