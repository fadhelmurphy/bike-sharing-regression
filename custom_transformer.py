from sklearn.base import TransformerMixin
import pandas as pd
from statsmodels.tools.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np

# Hitung VIF (Variance Inflation Factor) untuk mengukur multikolinieritas
def calculate_vif(data_frame, verbose=False):

    dropped_columns = []  # List untuk menyimpan kolom yang dihapus
    
    while True:
        vif_values = [variance_inflation_factor(data_frame.values, i) for i in range(data_frame.shape[1])]
        max_vif_index = np.argmax(vif_values)
        max_vif = max(vif_values)
        
        if max_vif > 5:
            column_to_drop = data_frame.columns[max_vif_index]
            dropped_columns.append(column_to_drop)  # Menyimpan kolom yang dihapus
            data_frame = data_frame.drop(column_to_drop, axis=1)
        else:
            break

    if verbose:
        vif_df = pd.DataFrame({
            'Feature': data_frame.columns,
            'VIF': vif_values
        })
        vif_df['Acceptance'] = np.where(vif_df['VIF'] <= 5, 'Yes', 'No')
        print(vif_df)
        print("\nKolom yang dapat dihapus : ")
        print(dropped_columns)
    return dropped_columns

class CustomFeatureTransformer(TransformerMixin):

    def __init__(self, param_transformer, cat_column, except_columns):
        self.param_transformer = param_transformer
        self.except_columns = except_columns
        self.cat_column = cat_column

    def fit(self, X, y=None, **fit_params):
        self.param_transformer.fit(X, y, **fit_params)
        return self

    def transform(self, X,**transform_params):
            # Transformasi data menggunakan ColumnTransformer
            X_transformed = self.param_transformer.transform(X, **transform_params)

            # Konversi hasil transformasi ke DataFrame
            transformed_columns = self.param_transformer.transformers_[0][1].get_feature_names_out(self.cat_column)
            columns = list(transformed_columns) + [col for col in X.columns if col not in self.cat_column]
            X_transformed_df = pd.DataFrame(X_transformed, columns=columns)

            # Menambahkan konstanta ke dalam DataFrame
            X_transformed_df = add_constant(X_transformed_df)

            # Hitung VIF untuk kolom numerik setelah transformasi
            get_dropped_column = calculate_vif(X_transformed_df, verbose = False)
            get_dropped_column = [kolom for kolom in get_dropped_column if kolom not in self.except_columns]
            X_transformed_df.drop(columns=get_dropped_column, inplace=True)
            self.feature_names = X_transformed_df.columns
            return X_transformed_df.values.tolist()

    def fit_transform(self, X, y=None, **fit_params):
            # Transformasi data menggunakan ColumnTransformer
            X_transformed = self.param_transformer.fit_transform(X, y, **fit_params)

            # Konversi hasil transformasi ke DataFrame
            transformed_columns = self.param_transformer.transformers_[0][1].get_feature_names_out(self.cat_column)
            columns = list(transformed_columns) + [col for col in X.columns if col not in self.cat_column]
            X_transformed_df = pd.DataFrame(X_transformed, columns=columns)

            # Menambahkan konstanta ke dalam DataFrame
            X_transformed_df = add_constant(X_transformed_df)

            # Hitung VIF untuk kolom numerik setelah transformasi
            get_dropped_column = calculate_vif(X_transformed_df, verbose = False)
            get_dropped_column = [kolom for kolom in get_dropped_column if kolom not in self.except_columns]
            X_transformed_df.drop(columns=get_dropped_column, inplace=True)
            self.feature_names = X_transformed_df.columns
            return X_transformed_df.values.tolist()
    
    def get_feature_names_out(self):
          return self.feature_names
