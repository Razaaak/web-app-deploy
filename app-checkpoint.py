{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "839cccbb-022b-4d78-b24d-cdc62dcec8a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "\n",
    "df = pd.read_csv(r'C:\\Users\\DELL\\Downloads\\beer-servings (1).csv')\n",
    "df.drop(columns=[\"Unnamed: 0\"], inplace=True)\n",
    "df.dropna(inplace=True)\n",
    "\n",
    "model = joblib.load(\"best_model.pkl\")\n",
    "\n",
    "\n",
    "st.title(\"Global Alcohol Consumption Predictor\")\n",
    "st.markdown(\"Predict **total litres of pure alcohol** consumed per person based on beverage servings and region.\")\n",
    "\n",
    "\n",
    "st.header(\"Data Insights\")\n",
    "\n",
    "col1, col2 = st.columns(2)\n",
    "\n",
    "with col1:\n",
    "    st.subheader(\"Average Alcohol Servings by Continent\")\n",
    "    continent_means = df.groupby(\"continent\")[[\"beer_servings\", \"spirit_servings\", \"wine_servings\"]].mean()\n",
    "    st.bar_chart(continent_means)\n",
    "\n",
    "with col2:\n",
    "    st.subheader(\"Total Pure Alcohol Distribution\")\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.histplot(df[\"total_litres_of_pure_alcohol\"], bins=20, kde=True, ax=ax)\n",
    "    st.pyplot(fig)\n",
    "\n",
    "\n",
    "st.header(\"Make a Prediction\")\n",
    "\n",
    "\n",
    "countries = sorted(df[\"country\"].unique())\n",
    "continents = sorted(df[\"continent\"].unique())\n",
    "\n",
    "country = st.selectbox(\"Select Country\", countries)\n",
    "continent = st.selectbox(\"Select Continent\", continents)\n",
    "beer_servings = st.number_input(\"Beer Servings\", min_value=0, max_value=500, value=100)\n",
    "spirit_servings = st.number_input(\"Spirit Servings\", min_value=0, max_value=500, value=50)\n",
    "wine_servings = st.number_input(\"Wine Servings\", min_value=0, max_value=500, value=30)\n",
    "\n",
    "input_data = pd.DataFrame({\n",
    "    \"country\": [country],\n",
    "    \"beer_servings\": [beer_servings],\n",
    "    \"spirit_servings\": [spirit_servings],\n",
    "    \"wine_servings\": [wine_servings],\n",
    "    \"continent\": [continent]\n",
    "})\n",
    "\n",
    "if st.button(\"Predict Alcohol Consumption\"):\n",
    "    prediction = model.predict(input_data)\n",
    "    st.success(f\" Estimated total litres of pure alcohol: **{prediction[0]:.2f}** per person/year\")\n",
    "\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.caption(\"Developed by [raz]. Data Source: WHO\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7e67541-62c0-4322-ba14-df9a6a042a05",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4edc2407-f7af-434a-a548-897fd5a4f277",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8573170-b9f7-4437-bf93-6bfba5a6a3c4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
