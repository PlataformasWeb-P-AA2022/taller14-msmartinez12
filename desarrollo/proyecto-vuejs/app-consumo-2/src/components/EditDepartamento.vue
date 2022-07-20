<!-- <template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="departamento">Departamento</label>
                <input type="text" class="form-control" id="departamento" v-model="departamento.departamento"
                    v-validate="'required'" name="departamento" placeholder="Ingrese departamento"
                    :class="{ 'is-invalid': errors.has('departamento.departamento') && submitted }">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="tipo">Tipo</label>
                <input type="text" class="form-control" id="Tipo" v-model="departamento.tipo" v-validate="'required'"
                    name="tipo" placeholder="Ingrese Tipo"
                    :class="{ 'is-invalid': errors.has('departamento.tipo') && submitted }">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="propietario">propietario</label>
                <select v-model="departamento.propietario">
                    <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}
                    </option>
                </select>
            </div>

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
                departamento: '',
                tipo: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getpropietariosList(),
            axios.get('http://127.0.0.1:8000/api/departamento/' + this.$route.params.id + '/')
                .then(response => {
                    console.log(response.data)
                    this.departamento = response.data
                });
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
                axios.put(`http://127.0.0.1:8000/api/departamento/${this.departamento.id}/`,
                    this.departamento
                )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script> -->
