<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costoDepartamento">Costo Departamento</label>
                <input type="text" class="form-control" id="costoDepartamento" v-model="departamento.costoDepartamento"
                    v-validate="'required'" name="costoDepartamento" placeholder="Ingrese Costo Departamento"
                    :class="{ 'is-invalid': errors.has('departamento.costoDepartamento') && submitted }">
                <div class="invalid-feedback">
                    Please provide a valid costo.
                </div>
            </div>

            <div class="form-group">
                <label for="numCuartos">Num Cuartos</label>
                <input type="text" class="form-control" id="numCuartos" v-model="departamento.numCuartos"
                    v-validate="'required'" name="numCuartos" placeholder="Ingrese Num Cuartos"
                    :class="{ 'is-invalid': errors.has('departamento.numCuartos') && submitted }">
                <div class="invalid-feedback">
                    Please provide a valid num cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="numBanios">Num Baños</label>
                <input type="text" class="form-control" id="numBanios" v-model="departamento.numBanios"
                    v-validate="'required'" name="numBanios" placeholder="Ingrese Num Bañios"
                    :class="{ 'is-invalid': errors.has('departamento.numBanios') && submitted }">
                <div class="invalid-feedback">
                    Please provide a valid num baños.
                </div>
            </div>

            <div class="form-group">
                <label for="valorAlicuota">Valor alicuato</label>
                <input type="text" class="form-control" v-model="departamento.valorAlicuota"
                    v-validate="'required'" name="valorAlicuota" placeholder="Ingrese Valor Alicuota"
                    :class="{ 'is-invalid': errors.has('departamento.valorAlicuota') && submitted }">
                <div class="invalid-feedback">
                    Please provide a valid valor alicuota.
                </div>
            </div>

            <div class="form-group">
                <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                    <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}
                    </option>
                </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costoDepartamento: '',
                numCuartos: '',
                numBanios: '',
                valorAlicuota: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getpropietariosList()
    },
    methods: {
        getpropietariosList() {
            axios
                .get('http://127.0.0.1:8000/api/propietario/')
                .then(response => {
                    this.propietariosList = response.data
                })
                .catch(error => {
                    console.log(error)
                })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamento/',
                    this.departamento
                )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
