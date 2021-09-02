<template>
  <div class="Sociodemografico">
    <div>
      <h2>Cuestionario Socio-Demográfico</h2>
    </div>

    <div class="codigo_participante">
      <h4 class="h4_question">1. Codigo del participante:</h4>
      <input
        class="question_input_text"
        type="text"
        id="nhcpaciente1"
        name="nhcpaciente"
        placeholder="Indica el número NHC"
        v-model="User.id_participante"
        style="width: 200px"
      />
    </div>
    <br />

    <div class="sexo">
      <h4>2. Sexo:</h4>
      <div class="radio_button_container">
        <input
          type="radio"
          id="genero1"
          name="genero"
          value="Hombre"
          v-model="User.sexo"
        />
        <label for="genero1">Hombre.</label>
        <br />
        <input
          type="radio"
          id="genero2"
          name="genero"
          value="Mujer"
          v-model="User.sexo"
        />
        <label for="genero2">Mujer.</label>
      </div>
      <br />
    </div>
    <br />
    <span
      >Elemento seleccionado: <strong>{{ User.sexo }}</strong></span
    >

    <div>
      <h4>3. Etnia:</h4>
      <input
        type="radio"
        id="etnia1"
        name="etnia"
        value="Caucásico o blanco."
        v-model="User.etnia"
      />
      <label for="etnia1">Caucásico o blanco.</label>
      <br />

      <input
        type="radio"
        id="etnia2"
        name="etnia"
        value="Americano o rojo (nativo americano)."
        v-model="User.etnia"
      />
      <label for="etnia2">Americano o rojo (nativo americano).</label>
      <br />

      <input
        type="radio"
        id="etnia3"
        name="etnia"
        value="Etiópico o negro."
        v-model="User.etnia"
      />
      <label for="etnia3">Etiópico o negro.</label>
      <br />

      <input
        type="radio"
        id="etnia4"
        name="etnia"
        value="Malayo o pardo (del sudeste de Asia)."
        v-model="User.etnia"
      />
      <label for="etnia4">Malayo o pardo (del sudeste de Asia).</label>
      <br />
      <input
        type="radio"
        id="etnia4"
        name="etnia"
        value="Mongólico o amarillo."
        v-model="User.etnia"
      />
      <label for="etnia4">Mongólico o amarillo.</label>
    </div>
    <br />
    <span
      >Elemento seleccionado: <strong>{{ User.etnia }}</strong></span
    >

    <div>
      <h4>4. Estado civil:</h4>

      <input
        type="radio"
        id="estadocivil1"
        name="estadocivil"
        value="Soltero/a."
        v-model="User.estadocivil"
      />
      <label for="estadocivil1">Soltero/a.</label>
      <br />

      <input
        type="radio"
        id="estadocivil2"
        name="estadocivil"
        value="Casado/a."
        v-model="User.estadocivil"
      />
      <label for="estadocivil2">Casado/a.</label>
      <br />

      <input
        type="radio"
        id="estadocivil3"
        name="estadocivil"
        value="Separado/a."
        v-model="User.estadocivil"
      />
      <label for="estadocivil3">Separado/a.</label>
      <br />

      <input
        type="radio"
        id="estadocivil4"
        name="estadocivil"
        value="Divorciado/a."
        v-model="User.estadocivil"
      />
      <label for="estadocivil4">Divorciado/a.</label>
      <br />

      <input
        type="radio"
        id="estadocivil5"
        name="estadocivil"
        value="Viudo."
        v-model="User.estadocivil"
      />
      <label for="estadocivil5">Viudo.</label>
    </div>
    <br />
    <span
      >Elemento seleccionado: <strong>{{ User.estadocivil }}</strong></span
    >

    <div>
      <h4>5. Nivel educativo:</h4>

      <input
        type="radio"
        id="estudios1"
        name="estudios"
        value="Bajo: Estudios
      preescolares, estudios de educación primaria, primera etapa de educación
      secundaria (1º- 2º ESO) ó FP básica."
        v-model="User.niveleducativo"
      />
      <label for="estudios1"
        >Bajo: Estudios preescolares, estudios de educación primaria, primera
        etapa de educación secundaria (1º- 2º ESO) ó FP básica.</label
      >
      <br />

      <input
        type="radio"
        id="estudios2"
        name="estudios"
        value="Medio: 3º-4º ESO
      ó Bachillerato ó Formación Profesional de grado medio."
        v-model="User.niveleducativo"
      />
      <label for="estudios2">
        Medio: 3º-4º ESO ó Bachillerato ó Formación Profesional de grado
        medio.</label
      >
      <br />

      <input
        type="radio"
        id="estudios3"
        name="estudios"
        value="Alto: Formación
      Profesional de grado superior, estudios universitarios, postgrado,
      doctorado."
        v-model="User.niveleducativo"
      />
      <label for="estudios3"
        >Alto: Formación Profesional de grado superior, estudios universitarios,
        postgrado, doctorado.</label
      >
    </div>
    <br />
    <span
      >Elemento seleccionado: <strong>{{ User.niveleducativo }}</strong></span
    >

    <div>
      <h4 class="h4_question">6. Profesión:</h4>
      <input
        class="question_input_text"
        type="text"
        id="profesion1"
        name="profesion"
        placeholder="Indica la profesión"
        v-model="User.profesion"
      />
    </div>
    <br />
    <span
      >Elemento seleccionado: <strong>{{ User.profesion }}</strong></span
    >

    <div>
      <h4>7. Situación profesional:</h4>
      <input
        type="radio"
        id="situacionprofesional1"
        name="situacionprofesional"
        value="Activo."
        v-model="User.situacionprofesional"
      />

      <label for="situacionprofesional1">Activo.</label>
      <br />

      <input
        type="radio"
        id="situacionprofesional2"
        name="situacionprofesional"
        value="Parado."
        v-model="User.situacionprofesional"
      />
      <label for="situacionprofesional2">Parado.</label>
      <br />

      <input
        type="radio"
        id="situacionprofesional3"
        name="situacionprofesional"
        value="Incapacidad Laboral Temporal (ILT)."
        v-model="User.situacionprofesional"
      />
      <label for="situacionprofesional3"
        >Incapacidad Laboral Temporal (ILT).</label
      >
      <br />

      <input
        type="radio"
        id="situacionprofesional4"
        name="situacionprofesional"
        value="Pensionista."
        v-model="User.situacionprofesional"
      />
      <label for="situacionprofesional4">Pensionista.</label>
      <br />

      <input
        type="radio"
        id="situacionprofesional5"
        name="situacionprofesional"
        value="Amo/a de casa."
        v-model="User.situacionprofesional"
      />
      <label for="situacionprofesional5">Amo/a de casa.</label>
      <br />

      <input
        type="radio"
        id="situacionprofesional6"
        name="situacionprofesional"
        value="Estudiante."
        v-model="User.situacionprofesional"
      />
      <label for="situacionprofesional6">Estudiante.</label>
      <br />

      <span
        >Elemento seleccionado:
        <strong>{{ User.situacionprofesional }}</strong></span
      >
    </div>
    <br />

    <div>
      <h4 class="h4_question">8. Población:</h4>
      <input
        class="question_input_text"
        type="text"
        id="poblacion"
        name="poblacion"
        placeholder="Poblacion"
        v-model="User.poblacion"
      />
    </div>
    <br />

    <span
      >Elemento seleccionado: <strong>{{ User.poblacion }}</strong></span
    >

    <div>
      <h4>9. Lugar de residencia:</h4>

      <input
        type="radio"
        id="residencia1"
        name="residencia"
        value="Urbano."
        v-model="User.residencia"
      />
      <label for="residencia1">Urbano.</label>

      <br />

      <input
        type="radio"
        id="residencia2"
        name="residencia"
        value="Rural."
        v-model="User.residencia"
      />
      <label for="residencia2">Rural.</label>
    </div>
    <br />

    <span
      >Elemento seleccionado: <strong>{{ User.residencia }}</strong></span
    >
    <br/>

    <div class="submit_button">
      <button type="submit" class="submit_button" @click="addToAPI">
        Guardar
      </button>
    </div>
  </div>
</template>


<script>
import axios from "axios";
axios.defaults.baseURL = "https://api.emosys.site";
// import VueAxios from 'vue-axios'

export default {
  name: "Sociodemografico",
  data() {
    return {
      User: {
        id_participante: " ",
        sexo: " ",
        etnia: " ",
        estadocivil: " ",
        niveleducativo: " ",
        profesion: " ",
        situacionprofesional: " ",
        poblacion: " ",
        lugarderesidencia: " ",
      },
    };
  },
  //Creating a local storage for the variables in the questionaire.
  mounted() {
    if (localStorage.id_participante) {
      this.id_participante = localStorage.User.id_participante;
    }
    // if (localStorage.sexo) {
    //   this.User.sexo = localStorage.sexo;
    // }
    // if (localStorage.etnia) {
    //   this.User.etnia = localStorage.etnia;
    // }
    // if (localStorage.estadocivil) {
    //   this.User.estadocivil = localStorage.estadocivil;
    // }
    // if (localStorage.niveleducativo) {
    //   this.User.niveleducativo = localStorage.niveleducativo;
    // }
    // if (localStorage.profesion) {
    //   this.User.profesion = localStorage.profesion;
    // }
    // if (localStorage.situacionprofesional) {
    //   this.User.situacionprofesional = localStorage.situacionprofesional;
    // }
    // if (localStorage.poblacion) {
    //   this.User.poblacion = localStorage.poblacion;
    // }
    // if (localStorage.residencia) {
    //   this.User.residencia = localStorage.residencia;
    // }
  },
  watch: {
    id_participante(newId_participante) {
      localStorage.id_participante = JSON.stringify(newId_participante);
    },
  },
  methods: {
    addToAPI() {
      let user = {
        id_participante: this.User.id_participante,
        sexo: this.User.sexo,
        etnia: this.User.etnia,
        estadocivil: this.User.estadocivil,
        niveleducativo: this.User.niveleducativo,
        profesion: this.User.profesion,
        situacionprofesional: this.User.situacionprofesional,
        poblacion: this.User.poblacion,
        lugarderesidencia: this.User.residencia,
      };
      console.log(JSON.stringify(user));
      axios
        .post("/users", {
          id: null,
          id_participante: user.id_participante,
          sexo: user.sexo,
          etnia: user.etnia,
          estadocivil: user.estadocivil,
          niveleducativo: user.niveleducativo,
          profesion: user.profesion,
          situacionprofesional: user.situacionprofesional,
          poblacion: user.poblacion,
          lugarderesidencia: user.lugarderesidencia,
        })
        .then((response) => console.log(response))
        .catch((error) => console.error(error));
      //Añadir una ventana emergente avisando que el participante ya esta dentro de la base de datos
    },
  },
};
</script>


<style scoped>
.h4_question {
  display: inline-block;
  margin-left: 5px;
}

.question_input_text {
  display: inline-block;
  margin-left: 10px;
}

.radio_button_container {
  display: inline-block;
  align-items: left;
  margin-top: 0px;
}

.codigo_participante {
  display: inline-block;
}
.sexo {
  display: inline-block;
}
.submit_button {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 5px 30px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px 5px;
  transition: background-color 0.5s;
}
.submit_button:hover {
  background-color: #467225;
}
</style>
