<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="telefono">Numero</label>
                <input
                    type="text"
                    class="form-control"
                    id="telefono"
                    v-model="telefono.telefono"
                    v-validate="'required'"
                    name="telefono"
                    placeholder="Ingres telefono"
                    :class="{'is-invalid': errors.has('telefono.telefono') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="tipo">Tipo</label>
                <input
                    type="text"
                    class="form-control"
                    id="Tipo"
                    v-model="telefono.tipo"
                    v-validate="'required'"
                    name="tipo"
                    placeholder="Ingrese Tipo"
                    :class="{'is-invalid': errors.has('telefono.tipo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="Propietario">Propietario</label>
                <select v-model="telefono.Propietario">
                            <option v-for="e in PropietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
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
            telefono: {
                telefono: '',
                tipo: '',
                Propietario: '',
            },
            PropietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList()
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietario/')
            .then(response => {
                this.PropietariosList = response.data
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
                        this.telefono
                    )
                    .then(response => {
                        this.$router.push('/telefonos');
                    })
            });
        }
    },
}
</script>
